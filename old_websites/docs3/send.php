
Thanks for your message!

<?php
    
    $userName         = $_POST['myName'];
    $userEmail         = $_POST['myEmail'];
    $userMessage         = $_POST['myMessage'];
    $to             = "bearhacksevhs@gmail.com";
    $subject         = "Email from my website";
    $body             = "Information Submitted:";
    $body .= "\r\n Name: " . $userName;
    $body .= "\r\n Email: " . $userEmail;
    $body .= "\r\n Message: " . $userMessage;
    mail($to, $subject, $body);
    ?>
