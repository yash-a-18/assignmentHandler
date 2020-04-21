<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>
		Login
	</title>
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  </head>
  <body style="background-color:powderblue;">

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
	
	
	<div class="container">
		<div class="row justify-content-start">
		    <div class="col-4">
		      <h2>Login</h2>
		    </div>
		</div>
	</div>



	<div class="alert alert-primary" role="alert">
		<div class="container">	
			<div class="row justify-content-end">
			    <div class="col-2">
					<a class="btn btn-outline-primary" href="Login.html" role="button">
						Home
					</a>
			    </div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Login.html" role="button">
					  	About
					  </a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Login.html" role="button">
					  	Courses
						</a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Login.html" role="button">
					  	Syllabus
					  </a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Login.html" role="button">
					  	Blog
						</a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Login.html" role="button">
					  	Contact
					  </a>
				</div>
			</div>
		</div>
	</div>
	<div class="container">
		<div class="row justify-content-start">
			<div class="alert alert-success" role="alert">
				  <h4 class="alert-heading">Well done!</h4>
				  <p>Aww yeah, you successfully read this important alert message.<br> 
					This example text is going to run a bit longer so that you can<br> 
					see how spacing within an alert works with this kind of content.</p>
				  <hr>
				  <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep<br> 
						things nice and tidy.</p>
			</div>
		</div>
	</div>



<center>
	<form action="" method="post">
	
	<div class="form-group row">
    <label for="user_email" class="col-sm-4 col-form-label">User Name</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="user_email" name="user_email" required>
    </div>
  </div>
	
	<div class="form-group row">
    <label for="user_password" class="col-sm-4 col-form-label">Password</label>
    <div class="col-sm-6">
      <input type="password" class="form-control" id="user_password" name="user_password" required>
    </div>
  </div>
	

  
  <button type="submit" class="btn btn-primary">Login</button>
  <br><strong>No Account???....<a href="registration/SignIn.html">Sign In</a></strong>
  
  </form>
</center>
</body>
</html>



<?php
if(isset($_POST["user_email"])&&isset($_POST["user_password"])){
	$dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
	//$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
	echo "Connection is established...<br/>";
	$dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
	$sql="select * from Users where user_email=?";
	
	$prepared_sql=$dbhandler->prepare($sql);
	$prepared_sql->execute(array($_POST["user_email"]));
	$row=$prepared_sql->fetch();
	echo "Connection is established...<br/>";
	
	if(strcmp($_POST["user_email"],$row["user_email"])==0&&strcmp($_POST["user_password"],$row["user_password"])==0){
		session_start();
		$_SESSION['user_email']=$_POST["user_email"];
		
		echo "success";
		if(strcmp($row["user_type"],'stu')==0){
			header('Location:/StudentHome.php?user_email='.$_POST["student_email"]);
		}
		else{
			header('Location:/TeacherHome.php?user_email='.$_POST["student_email"]);
		}
	}
	else{
		//header('Location:login.php?message=INVALID LOGIN DETAILS');
		echo "INVALID LOGIN DETAILS";
		header('Location:login.php');
	}
}
?>