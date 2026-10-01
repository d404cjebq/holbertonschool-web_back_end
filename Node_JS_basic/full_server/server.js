import express from 'express';
import router from './routes';

const app = express();
const PORT = 1245;

app.use('/', router);

app.listen(PORT, () => {
  console.log(`Server listening on PORT ${PORT}`);
});

export default app;
