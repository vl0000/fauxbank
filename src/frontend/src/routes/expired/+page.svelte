
<div class="page-container">
    <div class="container">
        <h1 class="session-expired">Session Expired</h1>
        <a class="back-to-login" href="/account">Return to Login</a>
    </div>
</div>


<style>

/* Outer container for background */
.page-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1f1f1f; /* Adjust the background color if needed */
}

/* Inner container for content */
.container {
  text-align: center;
}

/* Session Expired styling */
.session-expired {
  margin-top: 50px;
  color: white;
}

/* Back to Login (Button) styling */
.back-to-login {
  margin-top: 20px;
  display: inline-block;
  padding: 10px 20px;
  font-weight: bold;
  color: white;
  text-decoration: none;
  background-color: transparent;
  border: 2px solid white;
  border-radius: 5px;
  transition: background-color 0.1s, color 0.1s;
}

.back-to-login:active {
  background-color: white;
  color: black;
}


</style>