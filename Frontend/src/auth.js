// auth.js
export function saveToken(token) {
  localStorage.setItem("token", token);
}

export function getToken() {
  return localStorage.getItem("token");
}

export function authHeader() {
  const token = getToken();
  if (!token) return {};
  return { Authorization: `Bearer ${token}` };
}

export function logout() {
  localStorage.removeItem("token");
}
