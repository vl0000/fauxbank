<script>
    import { Preferences } from "@capacitor/preferences";
    import { api_url } from "../../stores";
    const endpoint = api_url + "/api/account/signup"

    let form;

    async function handle_submit() {
      const formData = new FormData(form)
      console.log('submit', formData)
      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          body: formData,
        });

        const data = await response.json();
        // Sets the jwt token for future usage
        await Preferences.set({key: "jwt", value:"Bearer " + data.access_token})


        // Print the response to the console
        console.log('Server Response:', data);
      } catch (error) {
        console.error('Error:', error);
      } finally {
        window.location.href = "/dashboard";
      }
    }

</script>
<div id="form-container">
  <form action="/" method="post" id="form" bind:this={form} on:submit|preventDefault={handle_submit}>
      <!-- This has to be named username anyways because of OAuth2 -->
      <input type="email" name="username" id="email" class="form-input">
      <input type="password" name="password" class="form-input" required>
      <div id="button-container">
        <input type="submit" value="Login" id="login-btn">
        <a href="/account/register">Or Sign up!</a>
      </div>

  </form>
</div>

<style>
.form-input {
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
  font-weight: 500;
  color: #585858;
  transition: border-color 0.3s, color 0.3s;
  width:100%;
}

.form-input:focus {
  outline: 2px solid black;
  border-color: black;
}

#login-btn {
  color: white;
  background-color: black;
  font-weight: bold;
  padding: 8px 16px; /* 2 pixels of padding top/bottom, 4 pixels of padding left/right */
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

#login-btn:hover {
  background-color: #333; /* Darker background on hover */
}
#form {
  display: inline-block;
  direction: column;
  width: 250px;
}
#form-container {
  display: flex;
  direction: column;
  align-items: center;
  justify-content: center;
  max-width: 100vw;
  height: 100vh;
  padding: auto;
}
#button-container {
  display: flex;
  direction: row;
  align-items: center;
  justify-content: space-around;
}
input{
  margin-top: 5px;
}
</style>