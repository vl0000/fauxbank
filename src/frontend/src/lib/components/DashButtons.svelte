<script>
</script>

<div class="dash-buttons">
    <a href="/dashboard/send" class="button">
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-arrow-up-right" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M14 2.5a.5.5 0 0 0-.5-.5h-6a.5.5 0 0 0 0 1h4.793L2.146 13.146a.5.5 0 0 0 .708.708L13 3.707V8.5a.5.5 0 0 0 1 0z"/>
        </svg>
    </a>
    <a href="/receive" class="button">
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-arrow-down-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2 13.5a.5.5 0 0 0 .5.5h6a.5.5 0 0 0 0-1H3.707L13.854 2.854a.5.5 0 0 0-.708-.708L3 12.293V7.5a.5.5 0 0 0-1 0z"/>
        </svg>
    </a>
    <a href="/scan" class="button">
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-qr-code-scan" viewBox="0 0 16 16">
            <path d="M0 .5A.5.5 0 0 1 .5 0h3a.5.5 0 0 1 0 1H1v2.5a.5.5 0 0 1-1 0zm12 0a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0V1h-2.5a.5.5 0 0 1-.5-.5M.5 12a.5.5 0 0 1 .5.5V15h2.5a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5v-3a.5.5 0 0 1 .5-.5m15 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1 0-1H15v-2.5a.5.5 0 0 1 .5-.5M4 4h1v1H4z"/>
            <path d="M7 2H2v5h5zM3 3h3v3H3zm2 8H4v1h1z"/>
            <path d="M7 9H2v5h5zm-4 1h3v3H3zm8-6h1v1h-1z"/>
            <path d="M9 2h5v5H9zm1 1v3h3V3zM8 8v2h1v1H8v1h2v-2h1v2h1v-1h2v-1h-3V8zm2 2H9V9h1zm4 2h-1v1h-2v1h3zm-4 2v-1H8v1z"/>
            <path d="M12 9h2V8h-2z"/>
          </svg>
    </a>
            
</div>

<style>
    .dash-buttons{
        display: grid;
        grid-template-columns: repeat(3, auto);
        column-gap: 12px;
        grid-template-rows: auto;
        padding-left: 10px;
        box-sizing: content-box;
        grid-area: dashbuttons;
        height: 100%;
        max-height: 90px;
        padding-left: 15px;

        scrollbar-width: none;
    }
    .dash-buttons::-webkit-scrollbar {
        display: none;
    }
    .dash-buttons:first-child {
        padding-left: 10px;
    }
    .button {
        grid-area: auto;

        height: 90px;
        width: 90px;


        background-color: black;
        border-radius: 10px;

        display: flex;
        direction: column;
        align-items: center;
        justify-content: center;
    }

    svg {
        fill: white;
    }
</style>