<?php
    if(/*empty($_POST['username'])||strlen($_POST['username'])>11*/0){
        echo "<h3>Enter name properly</h3>";
        echo "<br><a href=registration.php>retry</a>";
	}
    else if(/*strlen($_POST['newpass'])<6||strlen($_POST['newpass'])>10||strcmp($_POST['newpass'],$_POST['reenternewpass'])!=0*/0){
        echo "<h3>keep password length between 6 and 10,password missmatch</h3>";
        echo "<br><a href=registration.php>retry</a>";
    }
    else{

        //<!-- checking and uploading image file-->
        $student_email=$_POST['student_email'];
         
        //print_r($_FILES["student_image"]["name"]);
        if(empty ($_FILES["student_image"]["name"]))
        {
            echo "please upload image";
        }
        else{

            //###### validating user
            $dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
                //$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
            echo "Connection is established...<br/>";
            $dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
            
            $sql="select * from Student where student_email=?";
            $prepared_sql=$dbhandler->prepare($sql);
            //$query_result=$dbhandler->query($sql);
            $prepared_sql->execute(array($_POST["student_email"]));
            $row=$prepared_sql->fetch();
            if($row["student_email"]==$student_email){
                header('Location:../login.php?user_email='.$_POST["student_email"]);
            }

            //###### end validation


            if(!file_exists('uploads')) 
            {
                mkdir('uploads', 0777, true);
            }
            $base_dir_path="F:\\XAMP_server\htdocs\\PHP_LAB\\PHPAssignmentHandler\\uploads";
            
            if (!file_exists($base_dir_path.'\\'.$student_email)) 
            {
                mkdir($base_dir_path."\\".$student_email, 0777, true);
            }
            
            $target_location=$base_dir_path."\\".$student_email."\\".basename($_FILES["student_image"]["name"]);
            
            //<!-- file uploades-->   
            if(! (move_uploaded_file($_FILES["student_image"]["tmp_name"], $target_location))){//|($_FILES["student_image"]["size"]>300000)|(strcmp($_FILES["student_image"]["type"],'image/png')!=0)){
                echo "\nError0101: ".$_FILES["student_image"]["tmp_name"].", ".$target_location. $_FILES["student_image"]["error"] . "<br>size?:".$_FILES["student_image"]["size"]." png?:".strcmp($_FILES["student_image"]["type"],'image/png');
                die();
            }
            else
            {
                $ext = pathinfo($target_location, PATHINFO_EXTENSION);
                //$new=$base_dir_path.$student_email."/".basename($_FILES["student_image"]["name"]).".".$ext;
                $new=$base_dir_path."\\".$student_email."\\"."profile".".".$ext;
                echo "success-1";
                rename($target_location,$new);
                try{
                    $input_date=$_POST["student_dob"];
                    $date=date("Y-m-d H:i:s",strtotime($input_date));
                    
                    $sql="insert into Student"
                    . "(student_email,student_first_name,student_middle_name,student_last_name,student_dob,student_gender,student_semester,student_course,student_address,student_address2,student_city,student_state,student_zip,student_mobile_no,student_id_no) "
                    . "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
                    
                    //adding user and password in Users table
                    $sql2="insert into Users"
                    . "(user_email,user_password) "
                    . "values(?,?)";
                    $prepared_sql=$dbhandler->prepare($sql);
                    $prepared_sql2=$dbhandler->prepare($sql2);
                    $prepared_sql->execute(array($student_email,$_POST["student_first_name"],$_POST["student_middle_name"],$_POST["student_last_name"],$date,$_POST["student_gender"],$_POST["student_semester"],$_POST["student_course"],$_POST["student_address"],$_POST["student_address2"],$_POST["student_city"],$_POST["student_state"],$_POST["student_zip"],$_POST["student_mobile_no"],$_POST["student_id_no"]));
                    $prepared_sql2->execute(array($_POST["student_email"],$_POST["student_password"]));
                    echo "Data is inserted successfully";

                    session_start();
                    $_SESSION['user_email']=$_POST["student_email"];
                    echo "successfully registered";
                }
                catch(PDOException $e){
                    echo $row["student_email"];
                    echo $e->getMessage();
                    die();
                }
            }
        }
    }
    //header('Location:/login.php?user_email='.$_POST["student_email"]);
?> 