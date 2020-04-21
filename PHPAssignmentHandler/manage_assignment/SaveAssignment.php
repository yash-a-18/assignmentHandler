<?php
session_start();
if(isset($_SESSION['user_email'])){
    $dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
    //$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
    echo "Connection is established...<br/>";
    $dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    $ret_sql="select assign_id from Assignments where assign_name=? and c_id=?";
    $ret_prepared_sql=$dbhandler->prepare($ret_sql);
    $ret_prepared_sql->execute(array($_POST["assignment_name"],$_POST["course_assignment_id"]));
    $ret_row=$ret_prepared_sql->fetch();
    //echo $ret_row["assign_id"]
    if(!isset($ret_row["assign_id"])){
        //$dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
            //$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
        echo "Connection is established...<br/>";
        $dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
        try{
            $input_initial_date=$_POST["assignment_initial_date"];
            $init_date=date("Y-m-d H:i:s",strtotime($input_initial_date));
            $input_due_date=$_POST["assignment_due_date"];
            $due_date=date("Y-m-d H:i:s",strtotime($input_due_date));
            
            
            $sql="insert into Assignments"
            . "(assign_name,teacher_email,c_id,initial_date,due_date,max_size) "
            . "values(?,?,?,?,?,?)";
            
            $prepared_sql=$dbhandler->prepare($sql);
            $prepared_sql->execute(array($_POST["assignment_name"],$_POST["teacher_assignment_email"],$_POST["course_assignment_id"],$init_date,$due_date,$_POST["assignment_max_upload_size"]));
            echo "Creating Assignment";
            $ret_prepared_sql->execute(array($_POST["assignment_name"],$_POST["course_assignment_id"]));
            $ret_row=$ret_prepared_sql->fetch();
            echo $ret_row["assign_id"]."created successfully";
            echo "<a href='/login.html'>Home</a>";
            echo "<a href='AssignmentPage.html'>Add More Assignments</a>";
        }
        catch(PDOException $e){
            echo $e->getMessage();
            die();
        }
    }
    else{
        header("Location:AssignmentPage.html");
    }
}
else{
    header("Location:login.php?message=Please Login");
}
?>