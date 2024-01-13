<div class="grid-container">
<slot />
</div>

<style>

.grid-container {
    overflow-x: hidden;
    width: 100vw;
    max-width: 100vw;
    height: 100vh;
    display: grid;
    grid-template-columns: 100%;
    grid-template-rows: 2px minmax(90px, 100px) 220px 90px auto;
    row-gap: 8px;
    grid-template-areas:
    "nothing" 
    "balance"
    "card"
    "dashbuttons"
    "transactions"
    ;
}

</style>