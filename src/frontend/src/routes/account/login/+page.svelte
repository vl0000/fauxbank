<script>
    import { api_url } from "../../../stores";
    const endpoint = api_url + "/api/account/token"

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

      // Print the response to the console
      console.log('Server Response:', data);
    } catch (error) {
      console.error('Error:', error);
    }
  }

</script>
<div class="container text-center pt-3 px-5">
    <form action="/" method="post" id="form" class="q-flex" bind:this={form} on:submit|preventDefault={handle_submit}>
        <label for="email" class="form-label mt-2">Email Address</label>
        <input type="email" name="email" id="email" class="form-group">
        <label for="password" class="form-label mt-2">Password</label>
        <input type="password" name="password" class="form-group" required>
        <input type="submit" value="Login" id="login-btn" class="btn btn-primary mt-2">
    </form>
</div>