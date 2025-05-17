document.addEventListener('DOMContentLoaded', function() {
    const audioPlayer = document.getElementById('audio-player');
    const playButton = document.getElementById('play-button');
    const pauseButton = document.getElementById('pause-button');
    const seekBar = document.getElementById('seek-bar');
    const currentTime = document.getElementById('current-time');
    const duration = document.getElementById('duration');
    
    if (!audioPlayer) return;
    
    // 재생/일시정지 버튼 이벤트
    playButton.addEventListener('click', function() {
        audioPlayer.play();
        playButton.classList.add('hidden');
        pauseButton.classList.remove('hidden');
    });
    
    pauseButton.addEventListener('click', function() {
        audioPlayer.pause();
        pauseButton.classList.add('hidden');
        playButton.classList.remove('hidden');
    });
    
    // 시크바 업데이트
    audioPlayer.addEventListener('timeupdate', function() {
        const percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        seekBar.value = percent;
        
        // 시간 표시 업데이트
        const currentMinutes = Math.floor(audioPlayer.currentTime / 60);
        const currentSeconds = Math.floor(audioPlayer.currentTime % 60);
        currentTime.textContent = `${currentMinutes}:${currentSeconds < 10 ? '0' : ''}${currentSeconds}`;
    });
    
    // 오디오 로딩 완료시 전체 시간 표시
    audioPlayer.addEventListener('loadedmetadata', function() {
        const durationMinutes = Math.floor(audioPlayer.duration / 60);
        const durationSeconds = Math.floor(audioPlayer.duration % 60);
        duration.textContent = `${durationMinutes}:${durationSeconds < 10 ? '0' : ''}${durationSeconds}`;
    });
    
    // 시크바로 이동
    seekBar.addEventListener('change', function() {
        const time = audioPlayer.duration * (seekBar.value / 100);
        audioPlayer.currentTime = time;
    });
    
    // 재생 완료시
    audioPlayer.addEventListener('ended', function() {
        pauseButton.classList.add('hidden');
        playButton.classList.remove('hidden');
        seekBar.value = 0;
    });
}); 