<?php
session_start();
if(isset($_SESSION['user_email'])){
    $dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
    //$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
    echo "Connection is established...<br/>";
    
    $dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    
    $ret_sql="Update Submissions SET submission_marks_logic=?, submission_marks_uniqueness=? , submission_marks_quality=? where student_email=? and assign_id=? " ;
    $ret_prepared_sql=$dbhandler->prepare($ret_sql);
    try{
        $op=$ret_prepared_sql->execute(array($_POST["submission_marks_logic"],$_POST["submission_marks_uniqueness"],$_POST["submission_marks_quality"],$_POST["student_email"],$_POST["assign_id"]));
    //    echo "it worked".$op." "."<br>";
    }
    catch(PDOException $e){
        echo $e->getMessage();
        //    die();
    }
    //echo 'Location:ViewSubmissionList.php?asid='.$_POST["assign_id"]." ".$_POST["student_email"];
    header('Location:ViewSubmissionList.php?asid='.$_POST["assign_id"]);
    
}   
else{  
    header('Location:../login.php?user_email='.$_SESSION['user_email']);
}
    ?>