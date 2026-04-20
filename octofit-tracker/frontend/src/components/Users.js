// Verplaatst vanuit app/src/components/Users.js

import { useEffect } from "react";

export default function Users() {
  useEffect(() => {
    fetch("/api/users")
      .then((res) => res.json())
      .then((data) => {
        // Data verwerken indien nodig
      })
      .catch((err) => {
        // Foutafhandeling
      });
  }, []);
  return <div>Users component</div>;
}
