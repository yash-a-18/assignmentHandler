<?php
try{

	//$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
	$dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
	echo "Connection is established...<br/>";
	$dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
	$sql_students="create table Student (
        student_first_name VARCHAR(30) NOT NULL ,
        student_middle_name VARCHAR(30) NOT NULL ,
        student_last_name VARCHAR(30) NOT NULL ,
        student_dob datetime,
        student_gender VARCHAR(10) NOT NULL,
        student_semester VARCHAR(10) NOT NULL ,        
        student_email VARCHAR(100) NOT NULL unique,
        student_address VARCHAR(30) NOT NULL,
        student_address2 VARCHAR(30) NOT NULL,
        student_city VARCHAR(30) NOT NULL,
        student_state VARCHAR(30) NOT NULL,
        student_zip VARCHAR(10) NOT NULL,
        student_mobile_no VARCHAR(30) NOT NULL,
        student_id_no VARCHAR(30) NOT NULL,
        PRIMARY KEY (student_email)
        )";
        $query_student_table=$dbhandler->query($sql_students);
        echo "Student table successfully created<br>";
}catch(PDOException $e){
    echo "unable to create student<br>";
    //echo $e->getMessage();
//    die();
}
try{    
        $sql_teachers="create table Teacher (
            teacher_first_name VARCHAR(30) NOT NULL ,
            teacher_middle_name VARCHAR(30) NOT NULL ,
            teacher_last_name VARCHAR(30) NOT NULL ,
            teacher_dob datetime,
            teacher_gender VARCHAR(10) NOT NULL,
            teacher_email VARCHAR(100) NOT NULL unique,
            teacher_address VARCHAR(30) NOT NULL,
            teacher_address2 VARCHAR(30) NOT NULL,
            teacher_city VARCHAR(30) NOT NULL,
            teacher_state VARCHAR(30) NOT NULL,
            teacher_zip VARCHAR(10) NOT NULL,
            teacher_mobile_no VARCHAR(30) NOT NULL,
            teacher_id_no VARCHAR(30) NOT NULL,
            PRIMARY KEY (teacher_email)
            )";
        
    //remember to remove user when removing student 
    $query_teachers_table=$dbhandler->query($sql_teachers);
	echo "Teacher Table is created successfully<br>";	
}
catch(PDOException $e){
    echo "unable to create teachers<br>";
	//echo $e->getMessage();
//	die();
}
try{
    //remember to remove user when removing student 
    $sql_users="create table Users(
        user_email VARCHAR(100) NOT NULL PRIMARY KEY,
        user_password VARCHAR(15) NOT NULL,
        user_type VARCHAR(10) NOT ,
    )";
    $query_user_table=$dbhandler->query($sql_users);
    echo "<br>User Table is created successfully<br>";
}
catch(PDOException $e){
    echo "unable to create users<br>";
    //echo $e->getMessage();
//die();
}

try{    
    $sql_course="create table Courses (
        c_id VARCHAR(10) NOT NULL ,
        c_name VARCHAR(30) NOT NULL ,
        c_credit DECIMAL(5,2) NOT NULL ,
        PRIMARY KEY (c_id)
        )";
    
    $query_teachers_table=$dbhandler->query($sql_course);
    echo "<br>Course Table is created successfully<br>";	
}
catch(PDOException $e){
//echo $e->getMessage();
echo "unable to create course<br>";
//	die();
}


try{    
    $sql_assignment="create table Assignments (
        assign_id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
        assign_name VARCHAR(30) NOT NULL ,
        teacher_email VARCHAR(100) NOT NULL ,
        c_id VARCHAR(30) NOT NULL,
        initial_date datetime,
        due_date datetime,
        max_size INT(10),
        FOREIGN KEY (c_id) REFERENCES Courses(c_id) ON DELETE CASCADE
        )";
    
        //remember to remove user when removing student 
        $query_assign=$dbhandler->query($sql_assignment);
        echo "<br>table assignment is created successfully<br>";	
        }
        catch(PDOException $e){
            echo "unable to create assignments<br>";
            //echo $e->getMessage();
        //	die();
}
try{    
    $sql_stu_course="create table Teacher (
        student_email VARCHAR(100) NOT NULL unique,
        c_id VARCHAR(10) NOT NULL , 
        PRIMARY KEY (student_email,c_id)
        )";
    
//remember to remove user when removing student 
$query_teachers_table=$dbhandler->query($sql_teachers);
echo "Teacher Table is created successfully<br>";	
}
catch(PDOException $e){
echo "unable to create teachers<br>";
//echo $e->getMessage();
//	die();
}



?>