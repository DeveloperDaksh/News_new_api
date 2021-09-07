import { nanoid } from "@reduxjs/toolkit";

export default function ncNanoId(prefix = "nc_") {
  return prefix + nanoid() + nanoid();
}
