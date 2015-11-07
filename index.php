<!DOCTYPE html>

<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="keywords" content="i'm bored" />
		<meta name="description" content="" />
		<meta name="author" content="Mike Moniz" />
		<link rel="icon" type="image/x-icon" href="./assets/img/favicon.png" />
		
		<title>Birthday</title>
		
		<!-- FB Auth needs to be loaded with priority -->
		<script src="//connect.facebook.net/en_US/all.js"></script>
	</head>
	<body>
		<div id="fb-root"></div>
		<div>Hello world!</div>
		<div> user: 
<?php 
require './facebook/src/facebook.php';
/*FB APP Details*/
$app_id = '1564122003812488';
$secret = '54c1db851437ab0b93e23a091ab2c1bd';

/*Begin Session*/
session_start();


	// Create our Application instance (replace this with your appId and secret).
	$facebook = new Facebook(array(
	  'appId'  => $app_id,
	  'secret' => $secret,
	));

	// Get User ID
	$user_fb = $facebook->getUser();
	
	// We may or may not have this data based on whether the user is logged in.
	//
	// If we have a $user id here, it means we know the user is logged into
	// Facebook, but we don't know if the access token is valid. An access
	// token is invalid if the user logged out of Facebook.

	if ($user_fb) {
		try {
			// Proceed knowing you have a logged in user who's authenticated.
			$user_profile = $facebook->api('/me');
			$user_id = $user_profile["id"];
			
			echo $user_id;
			//id
			//first_name
			//gender => male
			//last_name
			//link
			//locale => en_US
			//name
			//timezone => -4
			//updated_time
			//verified
			
		} catch (FacebookApiException $e) {
			if (!$prod_request){
				echo "Exception occurred, code: " . $e->getCode();
				echo " with message: " . $e->getMessage();
			}
		}	
	} else {
		echo "no user";
	}

	// Login or logout url will be needed depending on current user state.
	if ($user_fb) {
	  $logoutUrl = $facebook->getLogoutUrl();
	} else {
	  $loginUrl = $facebook->getLoginUrl();
	}
	
?>
		</div>
	</body>
	<footer>
	</footer>
  </body>
</html>