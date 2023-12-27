<script>
    import { account } from "../../../stores";
</script>

<div class="row px-2 pt-2" id="info">
    <div class="col bg-primary-subtle">   
        <span>{$account.full_name}</span>
        <div class="d-flex">
            <span>{$account.agency}</span>
            <span class="px-3">{$account.account_number}</span>
        </div>
    </div>
</div>
<div class="row" id="settings">
<!-- Add settings here when i think of any -->
</div>