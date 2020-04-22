<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>
		View File
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
		      <h2>File</h2>
		    </div>
		</div>
	</div>



	<div class="alert alert-primary" role="alert">
		<div class="container">	
			<div class="row justify-content-end">
			    <div class="col-3">
					<a class="btn btn-outline-primary" href="/manageAssignments/TeacherHomePage.html" role="button">
						Home
					</a>
			    </div>
				<div class="col-3">
				      <a class="btn btn-outline-primary" href="/manageAssignments/TeacherAssignmentDisplay.html" role="button">
					  	Assignments
					  </a>
				</div>
				<div class="col-3">
				      <a class="btn btn-outline-primary" href="/Register/TeacherProfile.html" role="button">
					  	Profile
						</a>
				</div>
				<div class="col-3">
				      <a class="btn btn-outline-primary" href="/Register/Logout.html" role="button">
					  	Logout
					  </a>
				</div>
				<!--<div class="col-2">
				      <a class="btn btn-outline-primary" href="Login.html" role="button">
					  	Blog
						</a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Login.html" role="button">
					  	Contact
					  </a>
				</div>-->
			</div>
		</div>
	</div>
	<div class="container">
		<div class="row justify-content-start">
			<div class="alert alert-success" role="alert">
				  <h4 class="alert-heading"></h4>
				  <p>Aww yeah, you successfully read this important alert message.<br> 
					This example text is going to run a bit longer so that you can<br> 
					see how spacing within an alert works with this kind of content.</p>
				  <hr>
				  <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep<br> 
						things nice and tidy.</p>
			</div>
		</div>
	</div>
	



<br>
<p><strong><?php echo $_GET['filename'];   session_start();?></strong></p><br>
<div id="list">
    <p><iframe src="../uploads/<?php echo $_SESSION['user_email'];?>/<?php echo $_GET['filename'];?>" frameborder="1" height="400"
      width="95%"></iframe></p>
</div>

<br>
        <center>
	<form action="SetMarks.php" method="post" style="background-color:wheat">
	<div class="form-group row">
    <label for="submission_marks_logic" class="col-sm-4 col-form-label">Logic</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="submission_marks_logic" name="submission_marks_logic">
	</div>
  </div>
  <div class="form-group row">
    <label for=" submission_marks_uniqueness" class="col-sm-4 col-form-label">Uniqueness</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="submission_marks_uniqueness" name="submission_marks_uniqueness">
	</div>
  </div>
  <div class="form-group row">
    <label for="submission_marks_quality" class="col-sm-4 col-form-label">Quality</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="submission_marks_quality" name="submission_marks_quality">
      <input type="hidden" id="student_email" name="student_email" value="<?php echo $_GET['semail']; ?>">
      <input type="hidden" id="assign_id" name="assign_id" value="<?php echo $_GET['asid']; ?>">
	</div>
  </div>
	
<button type="submit" class="btn btn-primary" style="background-color:saddlebrown">Submit</button>
  
  </form>
</center>


</body>
</html>
