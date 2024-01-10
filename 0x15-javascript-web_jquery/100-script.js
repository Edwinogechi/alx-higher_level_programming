/* This script enhances the visual style of the <header> element by setting its text color to red (#FF0000)
   utilizing document.querySelector for element selection. */

document.addEventListener("DOMContentLoaded", function () {
  // Ensure the DOM is fully loaded before interacting with elements

  // Locate the <header> element in the document
  const headerElement = document.querySelector("header");

  // Confirm the existence of the targeted element
  if (headerElement) {
    // Adjust the text color to red
    headerElement.style.color = "#FF0000";
  }
});
