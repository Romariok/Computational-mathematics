import Button from '@mui/material/Button';

interface StyleButtonProps {
    type?: "button" | "submit" | "reset";
    fullWidth?: boolean;
    variant?: "text" | "outlined" | "contained";
    mt?: number;
    mb?: number;
    fontFamily?: string;
    backgroundColor?: string;
    color?: string;
    disabled?: boolean;
    onclick?: () => void;
    text: string;
}
export default function StyleButton(props: StyleButtonProps) {
   return (
      <Button
         type={props.type}
         fullWidth={props.fullWidth}
         variant={props.variant || "contained"}
         sx={{
            mt: props.mt || 3,
            mb: props.mb || 2,
            fontFamily: props.fontFamily || "Undertale",
            backgroundColor: props.backgroundColor || 'black',
            color: props.color || 'orange',
            ":hover": {
               backgroundColor: 'black',
               color: 'orange'
            },
            ":active": {
               backgroundColor: 'black',
               color: 'orange'
            },
            ":active:after": {
               backgroundColor: 'black',
               color: 'orange'
            }
         }}
         onClick={props.onclick}
         disabled={props.disabled}
      >
         {props.text}
      </Button>
   );
}
