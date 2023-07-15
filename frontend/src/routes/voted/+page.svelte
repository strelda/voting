<script lang='ts'>
    // Add your result page logic here
  </script>
  
  <style>
    .result-page {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      text-align: center;
    }
  
    .result-message {
      font-size: 24px;
      margin-bottom: 20px;
    }
  
    .return-button {
      padding: 10px 20px;
      background-color: rgb(35, 146, 70);
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 4px;
    }
  </style>
  
  <div class='result-page'>
    <p class="result-message">Congratulations, váš hlas byl zaznamenán.</p>
    <p>Pro nové hlasování se vraťte zpět.</p>
    <button class="return-button" on:click={() => window.history.back()}>Zpět</button>
  </div>
  