<script>
    export let title;

    // get real data from the server later
    const transactions = [-22.00, 500.0, -5.00];

</script>

<div class="transactions">
    <div id="title">
        <span>Latest Transactions</span>
        <a href="/"> Show all</a>
    </div>
    <ul id="transaction-list">
        {#each transactions as transaction}
            <li>
                <div class="info">
                    <div class="icon">
                        <!-- The SVG goes here-->
                    </div>
                    <span>YOU BOUGHT SOMETHING HUH</span>
                </div>
                <div class="movement">
                    {transaction}
                </div>
            </li>
        {/each}
    </ul>
</div>
<style>
    .transactions {
        height: 100%;   
        display: flex;
        flex-direction: column;
        border-radius: 32px 32px 0px 0px;
        height: 35vh;
        grid-area: transactions;
        padding: 15px;
        
        background-color: black;
        color: white;
    }
    .info {
        display: flex;
        direction: row;
        justify-content: space-evenly;
    }
    .icon {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: white;
        width: 45px;
        height: 45px;
        margin-right: 12px;

        border-radius: 6px;
    }

    #title {
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        margin-bottom: 15px;
        margin-top: 5px;
    }
    #transaction-list {
        padding-left: 0px;
    }
    #transaction-list > li {
        display: flex;
        direction: row;
        justify-content: space-between;

        list-style: none;
        margin-bottom: 5px;

        height: 45px

    }

</style>