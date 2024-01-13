<script>
import * as QRCode from 'qrcode'
import { account } from '../../stores';
    
let inputValue = "0.0";

async function generateQR() {
    let data = `{ "payee": ${$account.number}, "amount": ${inputValue}}`
    
    const canvas = document.getElementById('canvas')

    document.getElementById("form")?.classList.toggle("hidden")
    document.getElementById("canvas")?.classList.toggle("hidden")
    
    QRCode.toCanvas(canvas, data, (error) => console.error(error))
}

function handleClear() {
    // Handle clear button logic
    inputValue = "0.0";

}
</script>
<div id="container" >
    <canvas class="hidden" id="canvas"></canvas>
    <form id="form" class="form" action="" on:submit|preventDefault={generateQR}>
    <input type="number" class="form-input" name="amount" bind:value={inputValue} />
    <div class="button-container">
        <button class="submit-button">Generate</button>
        <button class="clear-button" on:click={handleClear}>Clear</button>
    </div>
    </form>
</div>

<style>
    .hidden {
        visibility: hidden;
        max-width: 1px;
        max-height: 1px;
    }
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
    #container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
    #canvas {
        height: 256px !important;
        width: 256px !important;
    }
</style>
