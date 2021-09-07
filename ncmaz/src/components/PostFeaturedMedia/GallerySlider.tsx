import Glide from "@glidejs/glide";
import NcImage from "components/NcImage/NcImage";
import NextPrev from "components/NextPrev/NextPrev";
import React, { FC, useEffect } from "react";
import ncNanoId from "utils/ncNanoId";

export interface GallerySliderProps {
  galleryImgs: string[];
}

const GallerySlider: FC<GallerySliderProps> = ({ galleryImgs }) => {
  const UNIQUE_CLASS = "glide_" + ncNanoId();

  useEffect(() => {
    if (!UNIQUE_CLASS) return;
    new Glide("." + UNIQUE_CLASS, {
      gap: 0,
      perView: 1,
    }).mount();
  }, []);

  return (
    <div className={`${UNIQUE_CLASS} group relative z-10 w-full h-full`}>
      <div className="glide__track h-full" data-glide-el="track">
        <ul className="glide__slides h-full">
          {galleryImgs.map((item, index) => (
            <li className="glide__slide h-full" key={index}>
              <NcImage src={item} containerClassName="w-full h-full" />
            </li>
          ))}
        </ul>
      </div>
      {/*  */}
      <div
        className="absolute opacity-0 group-hover:opacity-100 z-20 inset-x-2 top-1/2 transform -translate-y-1/2 flex justify-between glide__arrows"
        data-glide-el="controls"
      >
        <NextPrev onlyPrev btnClassName="w-8 h-8" />
        <NextPrev onlyNext btnClassName="w-8 h-8" />
      </div>
      {/*  */}
      <div className="absolute w-full left-0 bottom-0 h-8 bg-gradient-to-t from-neutral-700"></div>
      <div
        className="absolute z-10 bottom-3 left-0 w-full flex items-center justify-center glide__bullets"
        data-glide-el="controls[nav]"
      >
        {galleryImgs.map((_, index) => (
          <button
            key={index}
            className="glide__bullet w-1.5 h-1.5 bg-neutral-200 bg-opacity-70 rounded-full mx-0.5"
            data-glide-dir={`=${index}`}
          ></button>
        ))}
      </div>
    </div>
  );
};

export default GallerySlider;
