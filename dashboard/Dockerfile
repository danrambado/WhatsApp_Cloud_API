# # Dev stage
# FROM node:alpine as dev
# WORKDIR /app
# EXPOSE 3000
# CMD ["tail", "-f", "/dev/null"]



# Build stage
# Dev stage
FROM node:alpine as dev
WORKDIR /app
COPY ./dashboard/package.json ./dashboard/package-lock.json ./
RUN npm install
COPY ./dashboard ./
EXPOSE 3000
CMD ["npm", "run", "dev"]


# # Production stage
# FROM node:alpine as production
# ENV NODE_ENV=production
# WORKDIR /app
# COPY --from=build /app/package.json /app/package-lock.json ./
# RUN npm ci --only=production
# COPY --from=build /app/.next ./.next
# COPY --from=build /app/public ./public
# EXPOSE 3000
# CMD ["npm", "start"]
