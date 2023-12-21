<script>
    const data = {
        fullname: "FirstName LastName",
        agency: "00005",
        account: "0000000123",
    }
</script>

<div class="row px-2 pt-2" id="info">
    <div class="col bg-primary-subtle">   
        <span>{data.fullname}</span>
        <div class="d-flex">
            <span>{data.agency}</span>
            <span class="px-3">{data.account}</span>
        </div>
    </div>
</div>
<div class="row" id="settings">
<!-- Add settings here when i think of any -->
</div>