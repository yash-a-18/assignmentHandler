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
        $teacher_email=$_POST['teacher_email'];
         
        //print_r($_FILES["teacher_image"]["name"]);
        if(empty ($_FILES["teacher_image"]["name"]))
        {
            echo "please upload image";
        }
        else{

            //###### validating user
            $dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
                //$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
            echo "Connection is established...<br/>";
            $dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
            
            $sql="select * from teacher where teacher_email=?";
            $prepared_sql=$dbhandler->prepare($sql);
            //$query_result=$dbhandler->query($sql);
            $prepared_sql->execute(array($_POST["teacher_email"]));
            $row=$prepared_sql->fetch();
            if($row["teacher_email"]==$teacher_email){
                header('Location:../login.php?user_email='.$_POST["teacher_email"]);
            }

            //###### end validation


            if(!file_exists('uploads')) 
            {
                mkdir('uploads', 0777, true);
            }
            $base_dir_path="F:\\XAMP_server\htdocs\\PHP_LAB\\PHPAssignmentHandler\\uploads";
            
            if (!file_exists($base_dir_path.'\\'.$teacher_email)) 
            {
                mkdir($base_dir_path."\\".$teacher_email, 0777, true);
            }
            
            $target_location=$base_dir_path."\\".$teacher_email."\\".basename($_FILES["teacher_image"]["name"]);
            
            //<!-- file uploades-->   
            if(! (move_uploaded_file($_FILES["teacher_image"]["tmp_name"], $target_location))){//|($_FILES["teacher_image"]["size"]>300000)|(strcmp($_FILES["teacher_image"]["type"],'image/png')!=0)){
                echo "\nError0101: ".$_FILES["teacher_image"]["tmp_name"].", ".$target_location. $_FILES["teacher_image"]["error"] . "<br>size?:".$_FILES["teacher_image"]["size"]." png?:".strcmp($_FILES["teacher_image"]["type"],'image/png');
                die();
            }
            else
            {
                $ext = pathinfo($target_location, PATHINFO_EXTENSION);
                //$new=$base_dir_path.$teacher_email."/".basename($_FILES["teacher_image"]["name"]).".".$ext;
                $new=$base_dir_path."\\".$teacher_email."\\"."profile".".".$ext;
                echo "success-1";
                rename($target_location,$new);
                try{
                    $input_date=$_POST["teacher_dob"];
                    $date=date("Y-m-d H:i:s",strtotime($input_date));
                    
                    $sql="insert into teacher"
                    . "(teacher_email,teacher_first_name,teacher_middle_name,teacher_last_name,teacher_dob,teacher_gender,teacher_address,teacher_address2,teacher_city,teacher_state,teacher_zip,teacher_mobile_no,teacher_id_no) "
                    . "values(?,?,?,?,?,?,?,?,?,?,?,?,?)";
                    
                    //adding user and password in Users table
                    $sql2="insert into Users"
                    . "(user_email,user_password) "
                    . "values(?,?)";
                    $prepared_sql=$dbhandler->prepare($sql);
                    $prepared_sql2=$dbhandler->prepare($sql2);
                    $prepared_sql->execute(array($teacher_email,$_POST["teacher_first_name"],$_POST["teacher_middle_name"],$_POST["teacher_last_name"],$date,$_POST["teacher_gender"],$_POST["teacher_address"],$_POST["teacher_address2"],$_POST["teacher_city"],$_POST["teacher_state"],$_POST["teacher_zip"],$_POST["teacher_mobile_no"],$_POST["teacher_id_no"]));
                    $prepared_sql2->execute(array($_POST["teacher_email"],$_POST["teacher_password"]));
                    echo "Data is inserted successfully";

                    session_start();
                    $_SESSION['user_email']=$_POST["teacher_email"];
                    echo "successfully registered";
                }
                catch(PDOException $e){
                    echo $row["teacher_email"];
                    echo $e->getMessage();
                    die();
                }
            }
        }
    }
    //header('Location:/login.php?user_email='.$_POST["teacher_email"]);
?> 