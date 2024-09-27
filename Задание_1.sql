      SELECT c.login, COUNT(o.id) --если баг починили
      FROM "Couriers" AS c
      LEFT JOIN "Orders" AS o ON c.id = o."courierId"
      WHERE o."inDelivery" = true
      GROUP BY c.login;
