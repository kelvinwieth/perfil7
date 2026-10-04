import type { NextConfig } from "next";

const repoName = "perfil7";
const isGhPages = process.env.GITHUB_ACTIONS === "true" || process.env.GH_PAGES === "true";

const nextConfig: NextConfig = {
  output: "export",
  images: { unoptimized: true },
  basePath: isGhPages ? `/${repoName}` : "",
  assetPrefix: isGhPages ? `/${repoName}/` : undefined,
  trailingSlash: true,
};

export default nextConfig;
