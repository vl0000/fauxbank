<script>
    import { Preferences } from "@capacitor/preferences";
    import { api_url } from "../../../stores";

    let payee = 0;
    let inputValue = 0;

    async function handleSubmit() {
        // Handle form submission logic
        console.log('sent');
        await Preferences.get({key: "jwt"}).then(token => console.log(token))
        let resp = await fetch(
            api_url + "/api/payments",
            {
                method: 'POST',
                headers: {
                    cors: "no-cors",
                    "Content-Type": "application/json",
                    "Authorization": await Preferences.get({key: "jwt"}).then( (token) => token.value)

                },

                body: JSON.stringify({"payee": payee, "amount": inputValue})
            }
        ).then(res => console.log(res.json()))
    }

    function handleClear() {
        // Handle clear button logic
        inputValue = 0;
    }
</script>

<form class="form" action="" on:submit|preventDefault={handleSubmit}>
    <input type="number" class="form-input" name="payee" bind:value={payee} placeholder="Account number" />
    <input type="number" class="form-input" name="amount" bind:value={inputValue} placeholder="0.0" />
    <div class="button-container">
        <button class="submit-button">Send</button>
        <button class="clear-button" on:click={handleClear}>Clear</button>
    </div>
</form>

<style>
    .form {
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
        -webkit-appearance: none;
        appearance: textfield;
        text-align: right;
        margin-top: 5px;
    }

    .form-input:focus {
        outline: 2px solid black;
        border-color: black;
    }

    .button-container {
        display: flex;
        direction: row;
        align-items: center;
        justify-content: space-between;
        padding: 15px;
        width: 200px;
    }

    .submit-button,
    .clear-button {
        padding: 10px;
        font-size: 18px;
    }
</style>
