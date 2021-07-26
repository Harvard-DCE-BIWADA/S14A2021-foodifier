// SOURCE of help: https://www.youtube.com/watch?v=gA_HJMd7uvQ
(function(){
    var video = document.getElementById('video'),
        canvas = document.getElementById('canvas'),
        context = canvas.getContext('2d'),
        form_input = document.getElementById('linksub')
        photo = document.getElementById('photo')
        vendorUrl = window.URL || window.webkitURL;
    navigator.getMedia = navigator.getUserMedia ||
                        navigator.webkitGetUserMedia ||
                        navigator.mozGetUserMedia ||
                        navigator.msGetUserMedia;
    // Capture Video

    navigator.getMedia({
        video: true,
        audio: false
    }, function(stream){
        console.log(stream)
        video.srcObject = stream;
        video.play();
    }, function(error){
        //error
    });

    document.getElementById('capture').addEventListener('click', function() {
        context.drawImage(video, 0, 0, 380, 300)
        photo.setAttribute('src', canvas.toDataURL('image/jpg'));
        form_input.setAttribute('value', canvas.toDataURL('image/jpg'));
        console.log(form_input.getAttribute('value'))
    });

})();