import React from 'react';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';

import state, { bd } from '../appState';

export default function Step2() {
  return (
    <React.Fragment>
      <Typography variant="h6" gutterBottom>
         {"Вы ебливый пидорас по имени " + state.firstName + bd.Moskow}
      </Typography>
      <Grid container spacing={3}>

        <Grid item xs={12}>
          <FormControlLabel
            control={<Checkbox color="secondary" name="saveCard" value="yes" />}
            label= {"Вы ебливый пидорас по имени " + state.firstName + bd.Moskow}
          />
        </Grid>
      </Grid>
    </React.Fragment>
  );
}