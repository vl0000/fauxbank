<script>
    import { Preferences } from "@capacitor/preferences";

    import { api_url } from "../../../stores";
    
    let payee = "";
    let inputValue = 0;
  
    async function handleSubmit() {
      // Handle form submission logic
      let resp = await fetch(
        api_url + "/api/payments",
        {
            headers: {
                method: "POST",
                cors: "no-cors",
                Authorization: await Preferences.get({key: "jwt"}).then( (token) => token.value)
            },

            body: JSON.stringify({ payer:"", payee: payee, amount: inputValue })
        }
    // Later we will show an awaiting screen and tell the user whether or not this transaction was accepted
    ).then(resp => resp.json())
    }
  
    function handleClear() {
      // Handle clear button logic
      inputValue = 0;
    }
  </script>
  
  <div class="form-container">
    <form action="">
        <input type="number" class="form-input" bind:value={inputValue} on:submit|preventDefault={handleSubmit} />
        <div class="button-container">
            <button class="submit-button">Send</button>
            <button class="clear-button" on:click={handleClear}>Clear</button>
          </div>
    </form>
  

  </div>
  
  <style>
    .form-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 50vh;
    }
  
    .form-input {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 8px;
        font-weight: 500;
        color: #585858;
        transition: border-color 0.3s, color 0.3s;
        width:100%;
        -webkit-appearance: none;
        appearance: textfield;
        text-align: right;
    }

    .form-input:focus {
        outline: 2px solid black;
        border-color: black;
    }

  
    .button-container {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 15px;
    }
  
    .submit-button,
    .clear-button {
      padding: 10px;
      font-size: 18px;
      margin-right: 10px;
    }
  </style>
  