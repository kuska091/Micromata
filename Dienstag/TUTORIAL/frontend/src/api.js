const API_BASE_URL =
  "https://n7wbdyuzel.execute-api.eu-central-1.amazonaws.com/default";

export async function senden(pfad, methode = "GET", body, token) {
  const headers = {
    "Content-Type": "application/json",
  };

  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

  const route = pfad.startsWith("/") ? pfad : `/${pfad}`;

  const response = await fetch(`${API_BASE_URL}${route}`, {
    method: methode,
    headers,
    body: body !== undefined ? JSON.stringify(body) : undefined,
  });

  const data = await response.json().catch(() => ({}));

  return {
    status: response.status,
    data,
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