<div class="credit-card">
    <div id="card-info">
        <div id="chip">
            <svg width="40" height="30" viewBox="0 0 40 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M4 0C1.79086 0 0 1.79086 0 4V4.5H11C13.4853 4.5 15.5 6.51472 15.5 9V9.5H24.5V9C24.5 6.51472 26.5147 4.5 29 4.5H40V4C40 1.79086 38.2091 0 36 0H4ZM40 5.5H29C27.067 5.5 25.5 7.067 25.5 9V9.5V10V14.5H40V5.5ZM40 15.5V24.5H29C27.067 24.5 25.5 22.933 25.5 21V20.5V20V15.5H40ZM40 25.5V26C40 28.2091 38.2091 30 36 30H4C1.79086 30 0 28.2091 0 26V25.5H11C13.4853 25.5 15.5 23.4853 15.5 21V20.5H24.5V21C24.5 23.4853 26.5147 25.5 29 25.5H40ZM0 24.5H11C12.933 24.5 14.5 22.933 14.5 21V20.5V20V15.5H0V24.5ZM0 14.5H14.5V10V9.5V9C14.5 7.067 12.933 5.5 11 5.5H0V14.5ZM24.5 19.5H15.5V10.5H24.5V19.5Z" fill="white"/>
            </svg>
        </div>
        <small style="grid-area: exp">12/28</small>
        <span  style="grid-area: number; text-align: left;">****  ****  ****  1234</span>
        <strong style="grid-area: name; text-align: left;">Fulano de tal</strong>
        <div style="height: 40px; width: 100%; grid-area: logo;">
            <svg width="40" height="30" viewBox="0 0 171 108" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="54" cy="54" r="54" fill="#F14646"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M116.854 108C146.677 108 170.854 83.8234 170.854 54C170.854 24.1766 146.677 0 116.854 0C100.861 0 86.4919 6.95251 76.6042 18H92.8541V26H70.6713C69.1298 28.5371 67.7914 31.2113 66.6789 34H92.8541V42H64.1922C63.6021 44.6004 63.1998 47.272 63 50H92.8541V58H63C63.1998 60.728 63.6021 63.3996 64.1922 66H92.8541V74H66.6789C67.7914 76.7887 69.1298 79.4629 70.6713 82H92.8541V90H76.6042C86.4919 101.047 100.861 108 116.854 108Z" fill="#EAAA70"/>
                </svg>
        </div>
    </div>
</div>

<style>
    .credit-card {
        display: flex;  
        direction: column;
        align-items: end;

        grid-area: card;
        background-color: black;
        border-radius: 10px;
        margin: 0px 6px 0px 6px;
        padding: 0px 15px 40px 15px;
    }
    
    #card-info {
        align-items: end;
        text-align: center;
        color: white;
        display: grid;
        grid-template-columns: 85% 15%;
        grid-template-rows: 40px 40px 40px;
        row-gap: 10px;
        grid-template-areas: "chip n" "number exp" "name logo";

        width: 100%;
        height: 65%;
    }

    #chip {
        grid-area: chip;
        width: 50px;
        height: 40px;

        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>