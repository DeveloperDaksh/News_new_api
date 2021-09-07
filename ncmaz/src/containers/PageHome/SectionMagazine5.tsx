import React, { FC, useState } from "react";
import { PostDataType } from "data/types";
import HeaderFilter from "./HeaderFilter";
import useDemoTabFilter from "hooks/useDemoTabFilter";
import Card12 from "components/Card12/Card12";
import Card13 from "components/Card13/Card13";

export interface SectionMagazine5Props {
  tabs: string[];
  posts: PostDataType[];
  heading?: string;
}

const SectionMagazine5: FC<SectionMagazine5Props> = ({
  posts,
  tabs,
  heading = "Latest Articles 🎈 ",
}) => {
  let timeOut: NodeJS.Timeout | null = null;

  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [tabActive, setTabActive] = useState<string>(tabs[0]);

  const activePosts = useDemoTabFilter({
    isLoading,
    initPosts: posts,
    tabs,
    tabActive,
  });

  const handleClickTab = (item: string) => {
    if (item === tabActive) {
      return;
    }
    setIsLoading(true);
    setTabActive(item);
    if (timeOut) {
      clearTimeout(timeOut);
    }
    timeOut = setTimeout(() => {
      setIsLoading(false);
    }, 600);
  };

  return (
    <div className="nc-SectionMagazine5">
      <HeaderFilter
        tabActive={tabActive}
        tabs={tabs}
        heading={heading}
        onClickTab={handleClickTab}
      />
      {!activePosts.length && <span>Nothing we found!</span>}
      <div className="grid lg:grid-cols-2 gap-5 md:gap-7">
        {activePosts[0] && <Card12 post={activePosts[0]} />}
        <div className="grid gap-5 md:gap-7">
          {activePosts
            .filter((_, i) => i < 4 && i > 0)
            .map((item, index) => (
              <Card13 key={index} post={item} />
            ))}
        </div>
      </div>
    </div>
  );
};

export default SectionMagazine5;
