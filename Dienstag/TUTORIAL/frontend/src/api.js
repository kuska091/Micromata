export async function senden(pfad, methode = "GET", body, token) {
  const headers = {
    "Content-Type": "application/json"
  };

  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

  const response = await fetch(pfad, {
    method: methode,
    headers,
    body: body ? JSON.stringify(body) : undefined
  });

  const data = await response.json().catch(() => ({}));

  return {
    status: response.status,
    data
  };
}

export async function api(pfad, methode = "GET", body) {
  const token = sessionStorage.getItem("token");
  const response = await senden(pfad, methode, body, token);

  if (response.status === 401) {
    sessionStorage.clear();
    window.dispatchEvent(new Event("auth-expired"));
  }

  return response;
}