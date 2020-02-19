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
        student_course VARCHAR(30) NOT NULL,
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
        
    
    $sql_users="create table Users(
        user_email VARCHAR(100) NOT NULL PRIMARY KEY,
        user_password VARCHAR(15) NOT NULL,
        user_type VARCHAR(10) NOT NULL
    )";
    $query_student_table=$dbhandler->query($sql_students);
    $query_teachers_table=$dbhandler->query($sql_teachers);
    $query_user_table=$dbhandler->query($sql_users);
	echo "Table is created successfully";
	
}
catch(PDOException $e){
	echo $e->getMessage();
	die();
}
?>