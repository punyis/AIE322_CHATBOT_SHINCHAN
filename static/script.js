$('#send-btn').click(function(){
    var userMessage = $('#user-message').val();
    $('#chat-messages').append('<p class="chat-message user-message"><strong>คุณ:</strong> ' + userMessage + '</p>');
    
    $.ajax({
        url: '/ask',
        method: 'POST',
        data: { message: userMessage },
        success: function(response) {
            $('#chat-messages').append('<p class="chat-message bot-message"><strong>บอท:</strong> ' + response.response + '</p>');
            $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            $('#user-message').val('');
        }
    });
});
