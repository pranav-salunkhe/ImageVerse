<script>
  import { writable } from 'svelte/store';

  let d;
  let form = null; // Declare form as a regular variable, not a store
  let showViewButton = writable(false); // Svelte store to control the visibility of the button

  async function uploadImages() {
    const formData = new FormData(form);

    try {
      const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();
      console.log(data);

      d = data;
      showViewButton.set(true); // Set the store value to true
    } catch (error) {
      console.error('Error:', error);
    }
  }

  function viewImage() {
    if (d && d.status === 'success') {
      window.location.href = '/stylized';
    }
  }
</script>

<form id="imageForm" enctype="multipart/form-data" bind:this={form}>
  <label for="content_image">Select Content Image:</label>
  <input type="file" name="content_image" accept="image/*" required>
  
  <label for="style_image">Select Style Image:</label>
  <input type="file" name="style_image" accept="image/*" required>

  <button type="button" on:click={uploadImages}>Upload Images</button>
  {#if $showViewButton}
    <button type="button" id="viewBtn" on:click={viewImage}>View Image</button>
  {/if}
</form>

<style>
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }

  label {
    font-weight: bold;
  }

  button {
    margin-top: 10px;
    cursor: pointer;
  }
</style>
