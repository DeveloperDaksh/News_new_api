import React, { FC, useState } from "react";
import Card2 from "components/Card2/Card2";
import { PostDataType } from "data/types";
import Card6 from "components/Card6/Card6";
import HeaderFilter from "./HeaderFilter";
import useDemoTabFilter from "hooks/useDemoTabFilter";

export interface SectionMagazine1Props {
  tabs: string[];
  posts: PostDataType[];
  heading?: string;
  className?: string;
}

const SectionMagazine1: FC<SectionMagazine1Props> = ({
  posts,
  tabs,
  heading = "Latest Articles 🎈 ",
  className = "",
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
    <div className={`nc-SectionMagazine1 ${className}`}>
      <HeaderFilter
        tabActive={tabActive}
        tabs={tabs}
        heading={heading}
        onClickTab={handleClickTab}
      />
      {!activePosts.length && <span>Nothing we found!</span>}
      <div className="grid lg:grid-cols-2 gap-6 md:gap-8">
        {activePosts[0] && <Card2 size="large" post={activePosts[0]} />}
        <div className="grid gap-6 md:gap-8">
          {activePosts
            .filter((_, i) => i < 4 && i > 0)
            .map((item, index) => (
              <Card6 key={index} post={item} />
            ))}
        </div>
      </div>
    </div>
  );
};

export default SectionMagazine1;
