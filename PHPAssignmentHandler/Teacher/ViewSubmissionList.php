<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>
		Assignment Page
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
		      <h2>Home Page</h2>
		    </div>
		</div>
	</div>



	<div class="alert alert-primary" role="alert">
		<div class="container">	
			<div class="row justify-content-end">
			    <div class="col-2">
                                <a class="btn btn-outline-primary" href="TeacherHome.php" role="button">
						Home
					</a>
			    </div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Teacher_reg.html" role="button">
					  	About
					  </a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Teacher_reg.html" role="button">
					  	Courses
						</a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Teacher_reg.html" role="button">
					  	Syllabus
					  </a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Teacher_reg.html" role="button">
					  	Blog
						</a>
				</div>
				<div class="col-2">
				      <a class="btn btn-outline-primary" href="Teacher_reg.html" role="button">
					  	Contact
					  </a>
				</div>
			</div>
		</div>
	</div>

<?php
session_start();
if(isset($_SESSION['user_email'])){
    $dbhandler = new PDO('mysql:host=localhost:3306;dbname=ce4_13','root','');
    //$dbhandler = new PDO('mysql:host=192.168.29.150;dbname=ce4_13','ce4_13','ce4_13');
    echo "Connection is established...<br/>";
    $dbhandler->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    $ret_sql="select student_email,submission_date,submission_file_name,submission_marks_logic,submission_marks_uniqueness,submission_marks_quality from Submissions where assign_id=?" ;
    $ret_prepared_sql=$dbhandler->prepare($ret_sql);
    $ret_prepared_sql->execute(array($_GET["asid"]));
?>
<div class="container table-responsive">
  <h2>assignment List</h2>         
  <table class="table table-hover table-light">
    <thead>
      <tr>
          <th>Assignment ID</th>
        <th>Student Email</th>
        <th>Submission Date</th>
        <th>Logic Marks</th>
        <th>Uniqueness Marks</th>
        <th>Quality Marks</th>
        <th>Submitted File</th>
      </tr>
    </thead>
    <tbody>
     <?php while($ret_row=$ret_prepared_sql->fetch())
    {
?>  
      <tr>
        <td><?php echo $_GET['asid']; ?></td>
        <td><?php echo $ret_row['student_email']; ?></td>
        <td><?php echo $ret_row['submission_date']; ?></td>
        <td><?php echo $ret_row['submission_marks_logic']; ?></td>
        <td><?php echo $ret_row['submission_marks_uniqueness']; ?></td>
        <td><?php echo $ret_row['submission_marks_quality']; ?></td>
        <td><a href="ViewFile.php?semail=<?php echo $ret_row['student_email']; ?>&asid=<?php echo $_GET['asid']; ?>&foldername=<?php echo $ret_row['student_email']; ?>&filename=<?php echo $ret_row['submission_file_name']; ?>">View File</a></td>
      </tr>
    <?php }
}?>      
    </tbody>
  </table>
</div>  
  </body>
</html>
