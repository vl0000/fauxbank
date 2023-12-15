<script>
    export let title;

    // get real data from the server later
    const transactions = [-22.00, 500.0, -5.00];

</script>

<div class="transactionlist my-2">

    <span>{title}</span>
    <ul class="list-group mt-2">
        {#each transactions as transaction}
            <li class="list-group-item d-flex align-items-start justify-content-between ms-2">
                <span>ENTITY IMAGE</span>
                {#if transaction > 0}
                    <span class="text-success">+{transaction}</span>
                {:else}
                    <span class="text-danger">{transaction}</span>
                {/if}
            </li>
        {/each}
    </ul>
</div>
<style>
    .transactionlist {
        height: 30vh;
    }
</style>