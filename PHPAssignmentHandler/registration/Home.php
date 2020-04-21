<?php
session_start();
if(isset($_GET["user_email"])&&strcmp($_GET["user_email"],$_SESSION["user_email"])==0){
	$dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
	//$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
	echo "Connection is established...<br/>";
	$dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
	$sql="select * from assignments where user_email=?";
	
	$prepared_sql=$dbhandler->prepare($sql);
	$prepared_sql->execute(array($_POST["user_email"]));
	$row=$prepared_sql->fetch();
	echo "Connection is established...<br/>";
	
	if(true){
        

    }
}
?>