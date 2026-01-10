$(document).ready(function () {

    eel.init()()
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    });

    // sIRI cONFIGURATION
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude:"1",
    speed:"0.2",
    autostart: true
    })


    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
            sync: true,
        },
        out:{
            effect: "fadeOutUp",
            sync: true,
        },
    });

    // Mic Button click event

    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWavw").attr("hidden", false);
        eel.allCommands()()
    });


    function doc_keyUp(e) {
        if(e.key == 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWavw").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);


    // #display the message button
    function PlayAssistant(message) {
        // Add your implementation here
        if(message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWavw").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val('');
            $('#MicBtn').attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
    }


    function ShowHideMicButton(message) {
        if (message.length ==0) {
            $('#MicBtn').attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
        else {
            $('#MicBtn').attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }


    $('#chatbox').keyup(function (){

        let message = $('#chatbox').val();
        ShowHideMicButton(message);
    });

    $('#SendBtn').click(function () {
        let message = $('#chatbox').val();
        PlayAssistant(message);
    });


    $('#chatbox').keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $('#chatbox').val()
            PlayAssistant(message)
        }
    });





});

