function togglePassword(id, toggleBtn) {
  const input = document.getElementById(id);
  if (input.type === 'password') {
    input.type = 'text';
    toggleBtn.textContent = 'Ocultar';
  } else {
    input.type = 'password';
    toggleBtn.textContent = 'Mostrar';
  }
}
