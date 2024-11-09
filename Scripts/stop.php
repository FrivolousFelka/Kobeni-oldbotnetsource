<?php

    // Usage http://SERVERIP/endattk.php?Key=key
    
    $apikey = $_GET['Key'];
    
    if ($apikey != "Kobeni1337") {
    exit("Invailed APIKEY");
    }
    
    exec("pkill -f udp.py");
    exec("pkill -f icmp.py");
    exec("pkill -f nut.pl");
    exit("all attacks ended");
    
?>