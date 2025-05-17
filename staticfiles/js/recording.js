document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('start-recording');
    const stopButton = document.getElementById('stop-recording');
    const recordingsList = document.getElementById('recordings-list');
    const saveButton = document.getElementById('save-recording');
    
    if (!startButton) return;
    
    let mediaRecorder;
    let audioChunks = [];
    let audioBlob;
    let audioUrl;
    
    // 녹음 시작
    startButton.addEventListener('click', async function() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            
            mediaRecorder = new MediaRecorder(stream);
            
            mediaRecorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };
            
            mediaRecorder.onstop = () => {
                audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                audioUrl = URL.createObjectURL(audioBlob);
                
                const audioElement = document.createElement('audio');
                audioElement.src = audioUrl;
                audioElement.controls = true;
                
                recordingsList.innerHTML = '';
                recordingsList.appendChild(audioElement);
                
                saveButton.classList.remove('hidden');
            };
            
            mediaRecorder.start();
            startButton.classList.add('hidden');
            stopButton.classList.remove('hidden');
            
        } catch (err) {
            console.error('마이크 접근 오류:', err);
            alert('마이크 접근이 거부되었습니다. 녹음을 위해 마이크 접근을 허용해주세요.');
        }
    });
    
    // 녹음 정지
    stopButton.addEventListener('click', function() {
        mediaRecorder.stop();
        stopButton.classList.add('hidden');
        startButton.classList.remove('hidden');
    });
    
    // 녹음 저장
    saveButton.addEventListener('click', function() {
        const formData = new FormData();
        formData.append('audio_file', audioBlob, 'recording.wav');
        formData.append('lesson_id', document.getElementById('lesson-id').value);
        formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);
        
        fetch('/lessons/save-recording/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('녹음이 저장되었습니다!');
                window.location.href = `/lessons/${document.getElementById('lesson-id').value}/`;
            } else {
                alert('녹음 저장에 실패했습니다: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('저장 중 오류가 발생했습니다.');
        });
    });
}); 