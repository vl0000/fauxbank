<script>
    import { CameraPreview} from "@capacitor-community/camera-preview"
    import QrScanner from "qr-scanner"
    import { onMount } from "svelte"

    let decoded = "Awaiting"

    function goBack() {
        CameraPreview.stop()
        window.location.href = "/dashboard"
    }
    
    async function scan() {
        decoded = "awaiting"
        let data = await CameraPreview.capture({quality: 100})
        .then(result => "data:image/jpeg;base64," + result.value)
        
        let image = await fetch(data)
        .then(data => data.blob())
        .then(data => createImageBitmap(data))



        QrScanner.scanImage(image)
        .then(result => decoded = JSON.parse(result).amount)
        .catch(err => decoded = err)





    }
    onMount(
        () => CameraPreview.start({ parent: "cameraPreview", toBack: true})
    )

</script>
<div id="overlay">
</div>
<div id="button-container">
    <!-- For debugging purposes only-->
    <p contenteditable="true" bind:innerText={decoded}>{decoded}</p>
    <button class="button" on:click={scan}>Scan</button>
    <button class="button" on:click|preventDefault={goBack}>Back</button>
</div>
<div id="cameraPreview">

</div>
    


<style>
    :global(html) {
        background-color: transparent !important;
    }
    :global(body) {
        background-color: transparent !important;
    }
    #canv {
        background-color: black;
        position: absolute;
    }
    #button-container {
        background-color: transparent;
        width: 100%;
        height: 60px;
        position: absolute;
        transform: translate(-50%, -50%);
        top: 95%;
        left: 50%;

        display: flex;
        direction: row;
        align-items: center;
        justify-content: space-evenly;
    }
    #cameraPreview {
        background-color: transparent;
    }
    #overlay {
        background-color: transparent;
        height: 200px;
        width: 200px;
        border: dashed 4px rgba(235, 235, 235, 0.644);
        border-radius: 10px;
        position: absolute;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .button {
        padding: 5px 10px 5px 10px;
    }
</style>